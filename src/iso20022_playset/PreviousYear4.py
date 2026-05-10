from . import base_types
import YesNoIndicator
import PreviousYear1Choice

class PreviousYear4(base_types._BaseFieldType):

	__slots__ = ["_PrvsYrs", "_CshCmpntInd"]
	@property
	def PrvsYrs(self):
		return self._PrvsYrs

	@PrvsYrs.setter
	def PrvsYrs(self, value):
		self._PrvsYrs = value if type(value) != auto else self.make_default("PrvsYrs")

	@PrvsYrs.deleter
	def PrvsYrs(self):
		del self._PrvsYrs
		self._PrvsYrs = None

	@property
	def CshCmpntInd(self):
		return self._CshCmpntInd

	@CshCmpntInd.setter
	def CshCmpntInd(self, value):
		self._CshCmpntInd = value if type(value) != auto else self.make_default("CshCmpntInd")

	@CshCmpntInd.deleter
	def CshCmpntInd(self):
		del self._CshCmpntInd
		self._CshCmpntInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCmpntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

