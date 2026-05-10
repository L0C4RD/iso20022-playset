import base_types
import DerivativeClassification1
import Option14
import DerivativeUnderlyingLeg1

class Derivative3(base_types._BaseFieldType):

	__slots__ = ["_DerivUndrlygLeg", "_DerivClssfctn", "_OptnAttrbts"]
	@property
	def DerivUndrlygLeg(self):
		return self._DerivUndrlygLeg

	@DerivUndrlygLeg.setter
	def DerivUndrlygLeg(self, value):
		self._DerivUndrlygLeg = value if type(value) != auto else self.make_default("DerivUndrlygLeg")

	@DerivUndrlygLeg.deleter
	def DerivUndrlygLeg(self):
		del self._DerivUndrlygLeg
		self._DerivUndrlygLeg = None

	@property
	def DerivClssfctn(self):
		return self._DerivClssfctn

	@DerivClssfctn.setter
	def DerivClssfctn(self, value):
		self._DerivClssfctn = value if type(value) != auto else self.make_default("DerivClssfctn")

	@DerivClssfctn.deleter
	def DerivClssfctn(self):
		del self._DerivClssfctn
		self._DerivClssfctn = None

	@property
	def OptnAttrbts(self):
		return self._OptnAttrbts

	@OptnAttrbts.setter
	def OptnAttrbts(self, value):
		self._OptnAttrbts = value if type(value) != auto else self.make_default("OptnAttrbts")

	@OptnAttrbts.deleter
	def OptnAttrbts(self):
		del self._OptnAttrbts
		self._OptnAttrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivUndrlygLeg', type=DerivativeUnderlyingLeg1, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivClssfctn', type=DerivativeClassification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnAttrbts', type=Option14, min=0, max=1, mutex_group=None, array=False),
	))

