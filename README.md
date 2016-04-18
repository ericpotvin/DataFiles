# DataFile

Save data to a data file/binary file

## Params

- source: The source
- action: write or read
- search: The search criteria, index or key
- bin_file: The data/binary file

## Example

> python run.py --source phone --action read --search 561 --bin_file bin/nanpa.bin

### Phone

Create a data file for phone lookup

source: nanpa

#### The classification type of this ZIP Code.

Code and Description
- S: Non-Unique / Standard (all other ZIP codes)
- M: APO/FPO Military ZIP Code
- P: PO Box ZIP Code
- U: Unique/single high volume address

