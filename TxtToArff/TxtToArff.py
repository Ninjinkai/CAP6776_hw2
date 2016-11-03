# Homework 2 program to convert provided documents into Weka-usable .arff files.

# Create a list for input files and a list for output files.
input_path = []
output_path = []
# Insert files into the lists.
input_path.append('./hw2data/webkb-train-stemmed.txt')
input_path.append('./hw2data/webkb-test-stemmed.txt')
output_path.append('./arff/webkb-train-stemmed.arff')
output_path.append('./arff/webkb-test-stemmed.arff')

# Set of class labels, list containing all documents with labels.
class_labels = set()
documents = []

for doc_num in range(0, len(input_path)):

    # Read the input file into the document list.
    try:
        with open(input_path[doc_num], 'r') as input_file:
            for current_doc in input_file:
                documents.append(current_doc)
    except:
        error_message = 'File ' + input_path[doc_num] + ' not found.'
        exit(error_message)
    input_file.close()

    # Process each document in the list.
    for index, current_doc in enumerate(documents):
        # Split the first word from the rest of the document.
        temp_doc = current_doc.partition('\t')
        # Build the set of classes from the first word in each document
        class_labels.add(temp_doc[0])
        # Single quote around document, followed by a comma and class.
        current_doc = "'" + temp_doc[2].strip('\n') + "'," + temp_doc[0] + '\n'
        # Update the documents list.
        documents[index] = current_doc

    # Write the output file.
    with open(output_path[doc_num], 'w') as output_file:
        # Write the .arff file header.
        output_file.write(
            "@relation \'WebKB {0}\'\n\n@attribute Text string\n@attribute class-att {1}\n\n@data\n\n".format(
                input_path[doc_num].split('-')[1],
                str(sorted(class_labels)).replace("'", "").replace("[", "{").replace("]", "}")))
        # Write the documents to the file.
        for current_doc in documents:
            output_file.write("{0}".format(current_doc))
    output_file.close()

    documents = []
