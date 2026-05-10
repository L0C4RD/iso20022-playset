import base_types
import Percentage14Rate
import Number

class NumberOrPercentage2Choice(base_types._BaseFieldType):

	__slots__ = ["_ThrshldNb", "_ThrshldPctg"]
	@property
	def ThrshldNb(self):
		return self._ThrshldNb

	@ThrshldNb.setter
	def ThrshldNb(self, value):
		self._ThrshldNb = value if type(value) != auto else self.make_default("ThrshldNb")

	@ThrshldNb.deleter
	def ThrshldNb(self):
		del self._ThrshldNb
		self._ThrshldNb = None

	@property
	def ThrshldPctg(self):
		return self._ThrshldPctg

	@ThrshldPctg.setter
	def ThrshldPctg(self, value):
		self._ThrshldPctg = value if type(value) != auto else self.make_default("ThrshldPctg")

	@ThrshldPctg.deleter
	def ThrshldPctg(self):
		del self._ThrshldPctg
		self._ThrshldPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ThrshldNb', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ThrshldPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
	))

