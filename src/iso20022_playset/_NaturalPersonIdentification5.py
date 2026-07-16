# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalEntitySize1Code
from . import ExternalEntityType1Code
from . import GenericIdentification175
from . import IndustrySector3Choice
from . import Max500Text
from . import NPIIdentifier

class NaturalPersonIdentification5(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_NPI", "_NttySz", "_NttyTp", "_PrsnNm", "_Sctr"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', GenericIdentification175, False)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', GenericIdentification175, False)

	@property
	def NPI(self):
		return self._NPI

	@NPI.setter
	def NPI(self, value):
		self._NPI = value if value is not None else base_types.UninitialisedField(self, 'NPI', NPIIdentifier, False)

	@NPI.deleter
	def NPI(self):
		del self._NPI
		self._NPI = base_types.UninitialisedField(self, 'NPI', NPIIdentifier, False)

	@property
	def NttySz(self):
		return self._NttySz

	@NttySz.setter
	def NttySz(self, value):
		self._NttySz = value if value is not None else base_types.UninitialisedField(self, 'NttySz', ExternalEntitySize1Code, False)

	@NttySz.deleter
	def NttySz(self):
		del self._NttySz
		self._NttySz = base_types.UninitialisedField(self, 'NttySz', ExternalEntitySize1Code, False)

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if value is not None else base_types.UninitialisedField(self, 'NttyTp', ExternalEntityType1Code, False)

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = base_types.UninitialisedField(self, 'NttyTp', ExternalEntityType1Code, False)

	@property
	def PrsnNm(self):
		return self._PrsnNm

	@PrsnNm.setter
	def PrsnNm(self, value):
		self._PrsnNm = value if value is not None else base_types.UninitialisedField(self, 'PrsnNm', Max500Text, True)

	@PrsnNm.deleter
	def PrsnNm(self):
		del self._PrsnNm
		self._PrsnNm = base_types.UninitialisedField(self, 'PrsnNm', Max500Text, True)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', IndustrySector3Choice, True)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', IndustrySector3Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=GenericIdentification175, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NPI', type=NPIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttySz', type=ExternalEntitySize1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=ExternalEntityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnNm', type=Max500Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sctr', type=IndustrySector3Choice, min=0, max=None, mutex_group=None, array=True),
	))