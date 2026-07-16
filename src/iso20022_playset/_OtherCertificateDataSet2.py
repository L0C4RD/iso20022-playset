# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification1
from . import Exact4AlphaNumericText
from . import ISODate
from . import Max350Text
from . import Max35Text
from . import PartyIdentification26

class OtherCertificateDataSet2(base_types._BaseFieldType):

	__slots__ = ["_CertId", "_CertInf", "_CertTp", "_DataSetId", "_IsseDt", "_Issr"]
	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if value is not None else base_types.UninitialisedField(self, 'CertId', Max35Text, False)

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = base_types.UninitialisedField(self, 'CertId', Max35Text, False)

	@property
	def CertInf(self):
		return self._CertInf

	@CertInf.setter
	def CertInf(self, value):
		self._CertInf = value if value is not None else base_types.UninitialisedField(self, 'CertInf', Max350Text, True)

	@CertInf.deleter
	def CertInf(self):
		del self._CertInf
		self._CertInf = base_types.UninitialisedField(self, 'CertInf', Max350Text, True)

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if value is not None else base_types.UninitialisedField(self, 'CertTp', Exact4AlphaNumericText, False)

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = base_types.UninitialisedField(self, 'CertTp', Exact4AlphaNumericText, False)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification26, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification26, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertInf', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
	))