import base_types
import InvestorType4Code
import TargetMarket1Code

class TargetMarket5Choice(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Othr"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=InvestorType4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=TargetMarket1Code, min=0, max=1, mutex_group=1, array=False),
	))

