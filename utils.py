import pandas as pd

# Define the function to load the file, extract the dictionary, and then convert it to a pandas DataFrame
def load_and_convert_to_dataframe(file_path):
    def parse_hyperparam_accuracies(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data = []
        for line in lines:
            if "Evaluating combination" in line:
                params_part = line.split(':')[1].strip()
                lr = params_part.split(',')[0].split('=')[1].strip()
                weight_decay = params_part.split(',')[1].split('=')[1].strip()
                filter_size = params_part.split(',')[2].split('=')[1].strip()
            if "Output 1 Accuracy" in line:
                output_1_acc = line.split(',')[1].split(':')[1].strip()
                output_2_acc = line.split(',')[2].split(':')[1].strip()
                overall_acc = line.split(',')[3].split(':')[1].strip()

                data.append({
                    'LR': lr,
                    'Weight Decay': weight_decay,
                    'Filter Size': filter_size,
                    'Output 1 Accuracy': output_1_acc,
                    'Output 2 Accuracy': output_2_acc,
                    'Overall Accuracy': overall_acc
                })
        return data

    # Parse the file to get the data
    data = parse_hyperparam_accuracies(file_path)

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)

    return df

def highlight_max_accuracy(s):
    '''
    Highlights the highest overall accuracy in a DataFrame
    '''
    is_max = s == s.max()
    return ['font-weight: bold' if v else '' for v in is_max]

