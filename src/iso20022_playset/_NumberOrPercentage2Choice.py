from . import base_types
from ._Percentage14Rate import Percentage14Rate
from ._Number import Number

class NumberOrPercentage2Choice(base_types._BaseFieldType):

	__slots__ = ["_ThrshldPctg", "_ThrshldNb"]
	@property
	def ThrshldPctg(self):
		return self._ThrshldPctg

	@ThrshldPctg.setter
	def ThrshldPctg(self, value):
		self._ThrshldPctg = value if type(value) != base_types.auto else self.make_default("ThrshldPctg")

	@ThrshldPctg.deleter
	def ThrshldPctg(self):
		del self._ThrshldPctg
		self._ThrshldPctg = None

	@property
	def ThrshldNb(self):
		return self._ThrshldNb

	@ThrshldNb.setter
	def ThrshldNb(self, value):
		self._ThrshldNb = value if type(value) != base_types.auto else self.make_default("ThrshldNb")

	@ThrshldNb.deleter
	def ThrshldNb(self):
		del self._ThrshldNb
		self._ThrshldNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ThrshldPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ThrshldNb', type=Number, min=0, max=1, mutex_group=1, array=False),
	))

