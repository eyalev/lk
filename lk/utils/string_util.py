

def multi_command_template(command_template, separator=False, continue_on_error=False):

    if separator:

        separator_string = "echo; echo '-----------------------------------'; echo"

        replacement = ' &&\n' + separator_string + '\n'

        result = command_template.strip().replace('\n', replacement)

    else:

        if continue_on_error:
            result = command_template.strip().replace('\n', ' ;\n')
        else:
            result = command_template.strip().replace('\n', ' &&\n')

    return result
