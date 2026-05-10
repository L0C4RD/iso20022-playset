import base_types
import Max35Text
import Percentage14Rate

class AdditionalRightThreshold2Choice(base_types._BaseFieldType):

	__slots__ = ["_AddtlRghtThrshldPctg", "_AddtlRghtThrshld"]
	@property
	def AddtlRghtThrshldPctg(self):
		return self._AddtlRghtThrshldPctg

	@AddtlRghtThrshldPctg.setter
	def AddtlRghtThrshldPctg(self, value):
		self._AddtlRghtThrshldPctg = value if type(value) != auto else self.make_default("AddtlRghtThrshldPctg")

	@AddtlRghtThrshldPctg.deleter
	def AddtlRghtThrshldPctg(self):
		del self._AddtlRghtThrshldPctg
		self._AddtlRghtThrshldPctg = None

	@property
	def AddtlRghtThrshld(self):
		return self._AddtlRghtThrshld

	@AddtlRghtThrshld.setter
	def AddtlRghtThrshld(self, value):
		self._AddtlRghtThrshld = value if type(value) != auto else self.make_default("AddtlRghtThrshld")

	@AddtlRghtThrshld.deleter
	def AddtlRghtThrshld(self):
		del self._AddtlRghtThrshld
		self._AddtlRghtThrshld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRghtThrshldPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AddtlRghtThrshld', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

