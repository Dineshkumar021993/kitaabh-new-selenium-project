import pandas as pd
from datetime import datetime

# File paths
excel_file = 'C:\\Users\\Dinesh\\Downloads\\logistics_data.xlsx'
output_file = 'D:\\Tally\\logistics_tally_data.xml'

try:
    # Step 1: Read Excel data
    print("Reading Excel file...")
    df = pd.read_excel(excel_file)

    # Step 2: Validate required columns
    required_columns = ['Date', 'Party Name', 'Voucher Type', 'Ledger Name', 'Amount']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column in Excel: {col}")

    # Step 3: Start XML Envelope
    xml_data = '''<ENVELOPE>
  <HEADER>
    <TALLYREQUEST>Import Data</TALLYREQUEST>
  </HEADER>
  <BODY>
    <IMPORTDATA>
      <REQUESTDESC>
        <REPORTNAME>Vouchers</REPORTNAME>
      </REQUESTDESC>
      <REQUESTDATA>
'''

    # Step 4: Generate XML for each row
    print("Generating XML entries...")
    for index, row in df.iterrows():
        try:
            # Date conversion handling Timestamp or string
            if isinstance(row['Date'], pd.Timestamp):
                date = row['Date'].strftime('%Y%m%d')
            else:
                date = datetime.strptime(str(row['Date']), '%d/%m/%Y').strftime('%Y%m%d')

            party = str(row['Party Name']).strip()
            vtype = str(row['Voucher Type']).strip()
            ledger = str(row['Ledger Name']).strip()
            amount = float(row['Amount'])

            xml_data += f'''
      <TALLYMESSAGE xmlns:UDF="TallyUDF">
        <VOUCHER VCHTYPE="{vtype}" ACTION="Create">
          <DATE>{date}</DATE>
          <PARTYNAME>{party}</PARTYNAME>
          <VOUCHERTYPENAME>{vtype}</VOUCHERTYPENAME>
          <ALLLEDGERENTRIES.LIST>
            <LEDGERNAME>{ledger}</LEDGERNAME>
            <AMOUNT>{amount}</AMOUNT>
          </ALLLEDGERENTRIES.LIST>
        </VOUCHER>
      </TALLYMESSAGE>
    '''
        except Exception as e:
            print(f"Error in row {index + 2}: {e}")

    # Step 5: Close XML structure
    xml_data += '''
      </REQUESTDATA>
    </IMPORTDATA>
  </BODY>
</ENVELOPE>
'''

    # Step 6: Write XML to file
    with open(output_file, 'w') as f:
        f.write(xml_data)

    print(f"✅ Tally XML file generated: {output_file}")

except Exception as e:
    print(f"❌ Script failed: {e}")
