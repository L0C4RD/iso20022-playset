import base_types
import PercentageRate
import SpecialCollateral2Code
import SecuredCollateral2Choice

class Collateral18(base_types._BaseFieldType):

	__slots__ = ["_Valtn", "_SpclCollInd", "_Hrcut"]
	@property
	def Valtn(self):
		return self._Valtn

	@Valtn.setter
	def Valtn(self, value):
		self._Valtn = value if type(value) != auto else self.make_default("Valtn")

	@Valtn.deleter
	def Valtn(self):
		del self._Valtn
		self._Valtn = None

	@property
	def SpclCollInd(self):
		return self._SpclCollInd

	@SpclCollInd.setter
	def SpclCollInd(self, value):
		self._SpclCollInd = value if type(value) != auto else self.make_default("SpclCollInd")

	@SpclCollInd.deleter
	def SpclCollInd(self):
		del self._SpclCollInd
		self._SpclCollInd = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Valtn', type=SecuredCollateral2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCollInd', type=SpecialCollateral2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

