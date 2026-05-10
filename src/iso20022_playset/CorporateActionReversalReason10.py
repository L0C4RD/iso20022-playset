from . import base_types
import RestrictedFINXMax256Text
import CorporateActionReversalReason12Choice

class CorporateActionReversalReason10(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_AddtlRsnInf"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=CorporateActionReversalReason12Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRsnInf', type=RestrictedFINXMax256Text, min=0, max=1, mutex_group=None, array=False),
	))

