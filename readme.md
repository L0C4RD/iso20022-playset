![Banner](banner.png)

### 🧭 Quick navigation links
* [Overview](#overview)
* [Quickstart](#quickstart)
    * [Message parsing](#message-parsing)
    * [Message editing](#message-editing)
    * [Message validation](#message-validation)
    * [Message generation](#message-generation)
    * [Message serialisation/deserialisation](#message-serialisationdeserialisation)
* [Supported message classes](#supported-message-classes)

## Overview

The **ISO20022 Playset** is a swiss army knife for experimentation with ISO20022 messages. It's designed to be easy and intuitive to use, and aims to get your ISO20022 projects up and running as quickly as possible.

Here are some things it can do out of the box:

* [**Parse messages**](#message-parsing): Messages can be parsed from a variety of sources.
* [**Create and modify messages**](#message-editing): Messages can be created with user-supplied data, or fields in existing messages can be modified.
* [**Validate messages**](#message-validation): Messages can be validated against the ISO20022 schema.
* [**Generate sample messages**](#message-generation): Schema-compliant messages of a specified type can be generated with synthetic data.
* [**Serialise and deserialise messages**](#message-serialisationdeserialisation): *coming soon!*

## Quickstart

### Message parsing

#### Parse from file

```python
path_to_xml = os.path.join(".", "sample_msgs", "sample-tsmt-049-001-01.xml")
isomsg = iso20022.parse_file(path_to_xml)
print(type(isomsg))
```

#### Parse from string

```python
xml_string = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.002.001.14">
        <CstmrPmtStsRpt>
            <GrpHdr>
                <MsgId>ABC123</MsgId>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </GrpHdr>
            <OrgnlGrpInfAndSts>
                <OrgnlMsgId>XYZ456</OrgnlMsgId>
                <OrgnlMsgNmId>pain.001.001.03</OrgnlMsgNmId>
            </OrgnlGrpInfAndSts>
        </CstmrPmtStsRpt>
    </Document>
"""
isomsg = iso20022.parse_xml(xml_string)
print(type(isomsg))
```

#### Parse from ElementTree

```python
import defusedxml.ElementTree as ET

path_to_xml = os.path.join(".", "sample_msgs", "sample-tsmt-049-001-01.xml")
tree = ET.parse(path_to_xml)
isomsg = iso20022.parse_etree(tree)
print(type(isomsg))
```

#### Read specfic fields
```python
path_to_xml = os.path.join(".", "sample_msgs", "sample-tsmt-049-001-01.xml")
isomsg = iso20022.parse_file(path_to_xml)
print(isomsg.RoleAndBaselnAccptnc.TxId.Id.get())

```

### Message editing

#### Create message from scratch

```python
isomsg = iso20022.PAIN_002_001_14.Document("Document")

isomsg.CstmrPmtStsRpt = iso20022.auto()
isomsg.CstmrPmtStsRpt.GrpHdr = iso20022.auto()
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts = iso20022.auto()

isomsg.CstmrPmtStsRpt.GrpHdr.MsgId = iso20022.auto()
isomsg.CstmrPmtStsRpt.GrpHdr.MsgId.set("Example header msgid")

isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm = iso20022.auto()
isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm.set("1970-01-01T12:00:00")

isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId = iso20022.auto()
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId.set("Example original msgid")

isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId = iso20022.auto()
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId.set("pain.001.001.02")

print(isomsg.to_xml())
```

##### Output

```xml
<Document>
	<CstmrPmtStsRpt>
		<OrgnlGrpInfAndSts>
			<OrgnlMsgId>
				Example original msgid
			</OrgnlMsgId>
			<OrgnlMsgNmId>
				pain.001.001.02
			</OrgnlMsgNmId>
		</OrgnlGrpInfAndSts>
		<GrpHdr>
			<CreDtTm>
				1970-01-01T12:00:00
			</CreDtTm>
			<MsgId>
				Example header msgid
			</MsgId>
		</GrpHdr>
	</CstmrPmtStsRpt>
</Document>
```

#### Create message from scratch (manually defined fields)

Instead of using `auto()` as above, it is possible to manually define fields, as shown below.

```python
isomsg = iso20022.PAIN_002_001_14.Document("Document")

isomsg.CstmrPmtStsRpt = iso20022.CustomerPaymentStatusReportV14("CstmrPmtStsRpt")
isomsg.CstmrPmtStsRpt.GrpHdr = iso20022.GroupHeader128("GrpHdr")
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts = iso20022.OriginalGroupHeader22("OrgnlGrpInfAndSts")

isomsg.CstmrPmtStsRpt.GrpHdr.MsgId = iso20022.Max35Text("MsgId")
isomsg.CstmrPmtStsRpt.GrpHdr.MsgId.set("Example header msgid")

isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm = iso20022.ISODateTime("CreDtTm")
isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm.set("1970-01-01T12:00:00")

isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId = iso20022.Max35Text("OrgnlMsgId")
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId.set("Example original msgid")

isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId = iso20022.Max35Text("OrgnlMsgNmId")
isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId.set("pain.001.001.02")

print(isomsg.to_xml())
```

##### Output

```xml
<Document>
	<CstmrPmtStsRpt>
		<OrgnlGrpInfAndSts>
			<OrgnlMsgId>
				Example original msgid
			</OrgnlMsgId>
			<OrgnlMsgNmId>
				pain.001.001.02
			</OrgnlMsgNmId>
		</OrgnlGrpInfAndSts>
		<GrpHdr>
			<CreDtTm>
				1970-01-01T12:00:00
			</CreDtTm>
			<MsgId>
				Example header msgid
			</MsgId>
		</GrpHdr>
	</CstmrPmtStsRpt>
</Document>
```

#### Update message field

```python
xml_string = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
        <RsltnOfInvstgtn>
            <Assgnmt>
                <Id>RES123</Id>
                <Assgnr>
                    <Pty>
                        <Nm>AssigningBank</Nm>
                    </Pty>
                </Assgnr>
                <Assgne>
                    <Pty>
                        <Nm>ReceivingBank</Nm>
                    </Pty>
                </Assgne>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </Assgnmt>
            <Sts>
                <RjctdMod>
                    <Prtry>
                        ExampleString
                    </Prtry>
                </RjctdMod>
            </Sts>
        </RsltnOfInvstgtn>
    </Document>
"""
isomsg = iso20022.parse_xml(xml_string)
isomsg.RsltnOfInvstgtn.Sts.RjctdMod[0].Prtry.set("Some other string")
print(isomsg.to_xml())
```

##### Output

```xml
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
        <RsltnOfInvstgtn>
            <Assgnmt>
                <Id>RES123</Id>
                <Assgnr>
                    <Pty>
                        <Nm>AssigningBank</Nm>
                    </Pty>
                </Assgnr>
                <Assgne>
                    <Pty>
                        <Nm>ReceivingBank</Nm>
                    </Pty>
                </Assgne>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </Assgnmt>
            <Sts>
                <RjctdMod>
                    <Prtry>
                        Some other string
                    </Prtry>
                </RjctdMod>
            </Sts>
        </RsltnOfInvstgtn>
    </Document>
```

### Message validation

```python

xml_string = """
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
        <RsltnOfInvstgtn>
            <Assgnmt>
                <Id>RES123</Id>
                <Assgnr>
                    <Pty>
                        <Nm>AssigningBank</Nm>
                    </Pty>
                </Assgnr>
                <Assgne>
                    <Pty>
                        <Nm>ReceivingBank</Nm>
                    </Pty>
                </Assgne>
                <CreDtTm>1970-01-01T12:00:00</CreDtTm>
            </Assgnmt>
            <Sts>
                <RjctdMod>
                    <Prtry>
                        ExampleString
                    </Prtry>
                </RjctdMod>
            </Sts>
        </RsltnOfInvstgtn>
    </Document>
"""
isomsg = iso20022.parse_xml(xml_string)
isomsg.validate()

# Can detect invalid messages
isomsg.RsltnOfInvstgtn.Assgnmt.Id.set("A"*36) # This is a Max35Text field
try:
    isomsg.validate()
except iso20022.ValidateError as e:
    print(f"{str(e)}")

# Can validate whole message, or just individual sections or entries
isomsg.RsltnOfInvstgtn.Sts.validate()
isomsg.RsltnOfInvstgtn.Sts.RjctdMod[0].Prtry.validate()

```

### Message generation

```python

# Generate messages of a given type.
isomsg = iso20022.TSMT_049_001_01.Document("Document")
for _ in range(3):
    isomsg.generate()
    print(isomsg.to_xml())

```

### Message serialisation/deserialisation

*Coming soon!*


## Supported message classes

The **ISO20022 Playset** supports the following message classes:
