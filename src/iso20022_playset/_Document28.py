# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClassificationType4
from . import CountryCode
from . import Document26
from . import GenericIdentification190
from . import ISODateTime
from . import Max140Text
from . import PartyIdentification260Choice
from . import Period4Choice
from . import PositiveNumber
from . import SecurityIdentification49
from . import SupplementaryDataEnvelope1
from . import TransactionOperationType13Code
from . import TrueFalseIndicator

class Document28(base_types._BaseFieldType):

	__slots__ = ["_DataRcrd", "_DocRef", "_HomeCtry", "_HstCtry", "_HstrclData", "_PblctnPrd", "_PrsnlData", "_RgltryDataTp", "_RltdNtty", "_RltdPdctIdr", "_RltdPrd", "_RltdRgltryData", "_SubmissnDtTm", "_SubmissnTp", "_TechRcrdIdr", "_Vlntry", "_Vrsn"]
	@property
	def DataRcrd(self):
		return self._DataRcrd

	@DataRcrd.setter
	def DataRcrd(self, value):
		self._DataRcrd = value if value is not None else base_types.UninitialisedField(self, 'DataRcrd', SupplementaryDataEnvelope1, False)

	@DataRcrd.deleter
	def DataRcrd(self):
		del self._DataRcrd
		self._DataRcrd = base_types.UninitialisedField(self, 'DataRcrd', SupplementaryDataEnvelope1, False)

	@property
	def DocRef(self):
		return self._DocRef

	@DocRef.setter
	def DocRef(self, value):
		self._DocRef = value if value is not None else base_types.UninitialisedField(self, 'DocRef', Document26, True)

	@DocRef.deleter
	def DocRef(self):
		del self._DocRef
		self._DocRef = base_types.UninitialisedField(self, 'DocRef', Document26, True)

	@property
	def HomeCtry(self):
		return self._HomeCtry

	@HomeCtry.setter
	def HomeCtry(self, value):
		self._HomeCtry = value if value is not None else base_types.UninitialisedField(self, 'HomeCtry', CountryCode, False)

	@HomeCtry.deleter
	def HomeCtry(self):
		del self._HomeCtry
		self._HomeCtry = base_types.UninitialisedField(self, 'HomeCtry', CountryCode, False)

	@property
	def HstCtry(self):
		return self._HstCtry

	@HstCtry.setter
	def HstCtry(self, value):
		self._HstCtry = value if value is not None else base_types.UninitialisedField(self, 'HstCtry', CountryCode, True)

	@HstCtry.deleter
	def HstCtry(self):
		del self._HstCtry
		self._HstCtry = base_types.UninitialisedField(self, 'HstCtry', CountryCode, True)

	@property
	def HstrclData(self):
		return self._HstrclData

	@HstrclData.setter
	def HstrclData(self, value):
		self._HstrclData = value if value is not None else base_types.UninitialisedField(self, 'HstrclData', TrueFalseIndicator, False)

	@HstrclData.deleter
	def HstrclData(self):
		del self._HstrclData
		self._HstrclData = base_types.UninitialisedField(self, 'HstrclData', TrueFalseIndicator, False)

	@property
	def PblctnPrd(self):
		return self._PblctnPrd

	@PblctnPrd.setter
	def PblctnPrd(self, value):
		self._PblctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PblctnPrd', Period4Choice, False)

	@PblctnPrd.deleter
	def PblctnPrd(self):
		del self._PblctnPrd
		self._PblctnPrd = base_types.UninitialisedField(self, 'PblctnPrd', Period4Choice, False)

	@property
	def PrsnlData(self):
		return self._PrsnlData

	@PrsnlData.setter
	def PrsnlData(self, value):
		self._PrsnlData = value if value is not None else base_types.UninitialisedField(self, 'PrsnlData', TrueFalseIndicator, False)

	@PrsnlData.deleter
	def PrsnlData(self):
		del self._PrsnlData
		self._PrsnlData = base_types.UninitialisedField(self, 'PrsnlData', TrueFalseIndicator, False)

	@property
	def RgltryDataTp(self):
		return self._RgltryDataTp

	@RgltryDataTp.setter
	def RgltryDataTp(self, value):
		self._RgltryDataTp = value if value is not None else base_types.UninitialisedField(self, 'RgltryDataTp', ClassificationType4, True)

	@RgltryDataTp.deleter
	def RgltryDataTp(self):
		del self._RgltryDataTp
		self._RgltryDataTp = base_types.UninitialisedField(self, 'RgltryDataTp', ClassificationType4, True)

	@property
	def RltdNtty(self):
		return self._RltdNtty

	@RltdNtty.setter
	def RltdNtty(self, value):
		self._RltdNtty = value if value is not None else base_types.UninitialisedField(self, 'RltdNtty', PartyIdentification260Choice, True)

	@RltdNtty.deleter
	def RltdNtty(self):
		del self._RltdNtty
		self._RltdNtty = base_types.UninitialisedField(self, 'RltdNtty', PartyIdentification260Choice, True)

	@property
	def RltdPdctIdr(self):
		return self._RltdPdctIdr

	@RltdPdctIdr.setter
	def RltdPdctIdr(self, value):
		self._RltdPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'RltdPdctIdr', SecurityIdentification49, True)

	@RltdPdctIdr.deleter
	def RltdPdctIdr(self):
		del self._RltdPdctIdr
		self._RltdPdctIdr = base_types.UninitialisedField(self, 'RltdPdctIdr', SecurityIdentification49, True)

	@property
	def RltdPrd(self):
		return self._RltdPrd

	@RltdPrd.setter
	def RltdPrd(self, value):
		self._RltdPrd = value if value is not None else base_types.UninitialisedField(self, 'RltdPrd', Period4Choice, False)

	@RltdPrd.deleter
	def RltdPrd(self):
		del self._RltdPrd
		self._RltdPrd = base_types.UninitialisedField(self, 'RltdPrd', Period4Choice, False)

	@property
	def RltdRgltryData(self):
		return self._RltdRgltryData

	@RltdRgltryData.setter
	def RltdRgltryData(self, value):
		self._RltdRgltryData = value if value is not None else base_types.UninitialisedField(self, 'RltdRgltryData', GenericIdentification190, True)

	@RltdRgltryData.deleter
	def RltdRgltryData(self):
		del self._RltdRgltryData
		self._RltdRgltryData = base_types.UninitialisedField(self, 'RltdRgltryData', GenericIdentification190, True)

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if value is not None else base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	@property
	def SubmissnTp(self):
		return self._SubmissnTp

	@SubmissnTp.setter
	def SubmissnTp(self, value):
		self._SubmissnTp = value if value is not None else base_types.UninitialisedField(self, 'SubmissnTp', TransactionOperationType13Code, False)

	@SubmissnTp.deleter
	def SubmissnTp(self):
		del self._SubmissnTp
		self._SubmissnTp = base_types.UninitialisedField(self, 'SubmissnTp', TransactionOperationType13Code, False)

	@property
	def TechRcrdIdr(self):
		return self._TechRcrdIdr

	@TechRcrdIdr.setter
	def TechRcrdIdr(self, value):
		self._TechRcrdIdr = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdIdr', Max140Text, False)

	@TechRcrdIdr.deleter
	def TechRcrdIdr(self):
		del self._TechRcrdIdr
		self._TechRcrdIdr = base_types.UninitialisedField(self, 'TechRcrdIdr', Max140Text, False)

	@property
	def Vlntry(self):
		return self._Vlntry

	@Vlntry.setter
	def Vlntry(self, value):
		self._Vlntry = value if value is not None else base_types.UninitialisedField(self, 'Vlntry', TrueFalseIndicator, False)

	@Vlntry.deleter
	def Vlntry(self):
		del self._Vlntry
		self._Vlntry = base_types.UninitialisedField(self, 'Vlntry', TrueFalseIndicator, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', PositiveNumber, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataRcrd', type=SupplementaryDataEnvelope1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocRef', type=Document26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HomeCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstrclData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblctnPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryDataTp', type=ClassificationType4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdNtty', type=PartyIdentification260Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPdctIdr', type=SecurityIdentification49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRgltryData', type=GenericIdentification190, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnTp', type=TransactionOperationType13Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdIdr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vlntry', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))