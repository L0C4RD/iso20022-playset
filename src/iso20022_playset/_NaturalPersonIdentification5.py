# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ExternalEntitySize1Code import ExternalEntitySize1Code
from ._ExternalEntityType1Code import ExternalEntityType1Code
from ._GenericIdentification175 import GenericIdentification175
from ._IndustrySector3Choice import IndustrySector3Choice
from ._Max500Text import Max500Text
from ._NPIIdentifier import NPIIdentifier

class NaturalPersonIdentification5(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_NPI", "_NttySz", "_NttyTp", "_PrsnNm", "_Sctr"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != base_types.auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

	@property
	def NPI(self):
		return self._NPI

	@NPI.setter
	def NPI(self, value):
		self._NPI = value if type(value) != base_types.auto else self.make_default("NPI")

	@NPI.deleter
	def NPI(self):
		del self._NPI
		self._NPI = None

	@property
	def NttySz(self):
		return self._NttySz

	@NttySz.setter
	def NttySz(self, value):
		self._NttySz = value if type(value) != base_types.auto else self.make_default("NttySz")

	@NttySz.deleter
	def NttySz(self):
		del self._NttySz
		self._NttySz = None

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if type(value) != base_types.auto else self.make_default("NttyTp")

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = None

	@property
	def PrsnNm(self):
		return self._PrsnNm

	@PrsnNm.setter
	def PrsnNm(self, value):
		self._PrsnNm = value if type(value) != base_types.auto else self.make_default("PrsnNm")

	@PrsnNm.deleter
	def PrsnNm(self):
		del self._PrsnNm
		self._PrsnNm = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != base_types.auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=GenericIdentification175, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NPI', type=NPIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttySz', type=ExternalEntitySize1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=ExternalEntityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnNm', type=Max500Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sctr', type=IndustrySector3Choice, min=0, max=None, mutex_group=None, array=True),
	))