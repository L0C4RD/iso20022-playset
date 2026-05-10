from . import base_types
import SettlementFailsJustification1
import TrueFalseIndicator

class SettlementFailsDerogation1(base_types._BaseFieldType):

	__slots__ = ["_ElgbltyInd", "_Justfn"]
	@property
	def ElgbltyInd(self):
		return self._ElgbltyInd

	@ElgbltyInd.setter
	def ElgbltyInd(self, value):
		self._ElgbltyInd = value if type(value) != auto else self.make_default("ElgbltyInd")

	@ElgbltyInd.deleter
	def ElgbltyInd(self):
		del self._ElgbltyInd
		self._ElgbltyInd = None

	@property
	def Justfn(self):
		return self._Justfn

	@Justfn.setter
	def Justfn(self, value):
		self._Justfn = value if type(value) != auto else self.make_default("Justfn")

	@Justfn.deleter
	def Justfn(self):
		del self._Justfn
		self._Justfn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgbltyInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Justfn', type=SettlementFailsJustification1, min=0, max=1, mutex_group=None, array=False),
	))

