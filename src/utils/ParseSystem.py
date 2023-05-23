# File: ParseSystem.py
#
# A class that allows you to safely parse data into another type.
# Useful when we are going to read data from files like <.env>

class ParseSystem:

    # A method that allows you to change the data type from string to any other.
    # Parameter values of type other than <str> will not change.
    # The values themselves of the likes of [True, False, None] can be written in wrong and the algorithm i
    # will be able to react accordingly anyway.
    @staticmethod
    def auto_parse(_val: any) -> any:
        if isinstance(_val, str):
            match _val.lower():
                case 'true':
                    return True
                case 'false':
                    return False
                case 'none':
                    return None

            # Rejects spelling errors
            try:
                return eval(_val)
            except NameError:
                return _val

        else:
            return _val

    # Python allows you to replace any type of variable with <str>.
    @staticmethod
    def to_string(_val) -> str:
        return str(_val)
