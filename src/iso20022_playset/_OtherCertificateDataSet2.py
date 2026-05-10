from . import base_types
from ._Max350Text import Max350Text
from ._PartyIdentification26 import PartyIdentification26
from ._DocumentIdentification1 import DocumentIdentification1
from ._Max35Text import Max35Text
from ._Exact4AlphaNumericText import Exact4AlphaNumericText
from ._ISODate import ISODate

class OtherCertificateDataSet2(base_types._BaseFieldType):

	__slots__ = ["_IsseDt", "_Issr", "_CertId", "_CertInf", "_DataSetId", "_CertTp"]
	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if type(value) != base_types.auto else self.make_default("CertId")

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = None

	@property
	def CertInf(self):
		return self._CertInf

	@CertInf.setter
	def CertInf(self, value):
		self._CertInf = value if type(value) != base_types.auto else self.make_default("CertInf")

	@CertInf.deleter
	def CertInf(self):
		del self._CertInf
		self._CertInf = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != base_types.auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if type(value) != base_types.auto else self.make_default("CertTp")

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertInf', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
	))

