import argparse
import yaml
from parser.parser import NewsParser


def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description='News Parser')
    parser.add_argument('--config', required=True, help='Path to config file')
    args = parser.parse_args()

    config = load_config(args.config)
    np = NewsParser(config)
    np.run()


if __name__ == '__main__':
    main()
