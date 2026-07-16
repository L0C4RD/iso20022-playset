# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISO3NumericCountryCode
from . import LocalData14
from . import Max35Text
from . import Max99Text

class PartyIdentification285(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_Assgnr", "_Ctry", "_Id", "_LclData", "_LglCorpNm", "_ShrtNm"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', AdditionalData1, True)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', AdditionalData1, True)

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', Max35Text, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', Max35Text, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', ISO3NumericCountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', ISO3NumericCountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData14, True)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData14, True)

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'LglCorpNm', Max99Text, False)

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = base_types.UninitialisedField(self, 'LglCorpNm', Max99Text, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))