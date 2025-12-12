import re
import yaml

def main():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
        players = "|".join(config["players"])
        server_tags = "|".join(config["server_tags"])

    # RegEx patterns
    re_server_tag = re.compile(f"^{server_tags}")
    re_players = re.compile(f"^({players})")
    re_reactions = re.compile(":.*:")
    re_commands = re.compile("^(Add Reaction|Click to react|Reply|Forward|More|Edit)")
    re_dates = re.compile("\w*\d*,\s\d")
    re_edited = re.compile("\(edited\)")

    patterns = [re_server_tag, re_players, re_reactions, re_commands, re_dates, re_edited]

    with open("scene.txt", "r") as infile:
        lines = infile.readlines()
        unwanted_lines = []

        for pattern in patterns:
            unwanted_lines.extend([line for line in lines if pattern.search(line)])

        # Get list of lines without any undesired patterns
        lines = [line for line in lines if line not in unwanted_lines]
    
    with open("cleaned_scene.txt", "w") as outfile:
        outfile.writelines(lines)

if __name__ == "__main__":
    main()