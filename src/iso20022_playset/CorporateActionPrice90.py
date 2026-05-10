import base_types
import PriceFormat61Choice
import PriceFormat81Choice
import PriceFormat80Choice

class CorporateActionPrice90(base_types._BaseFieldType):

	__slots__ = ["_MaxPric", "_CshInLieuOfShrPric", "_MinMltplCshToInst", "_MinCshToInst", "_MinPric", "_LastBidIncrmtPric", "_OverSbcptDpstPric", "_FrstBidIncrmtPric", "_MaxCshToInst"]
	@property
	def MaxPric(self):
		return self._MaxPric

	@MaxPric.setter
	def MaxPric(self, value):
		self._MaxPric = value if type(value) != auto else self.make_default("MaxPric")

	@MaxPric.deleter
	def MaxPric(self):
		del self._MaxPric
		self._MaxPric = None

	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if type(value) != auto else self.make_default("CshInLieuOfShrPric")

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = None

	@property
	def MinMltplCshToInst(self):
		return self._MinMltplCshToInst

	@MinMltplCshToInst.setter
	def MinMltplCshToInst(self, value):
		self._MinMltplCshToInst = value if type(value) != auto else self.make_default("MinMltplCshToInst")

	@MinMltplCshToInst.deleter
	def MinMltplCshToInst(self):
		del self._MinMltplCshToInst
		self._MinMltplCshToInst = None

	@property
	def MinCshToInst(self):
		return self._MinCshToInst

	@MinCshToInst.setter
	def MinCshToInst(self, value):
		self._MinCshToInst = value if type(value) != auto else self.make_default("MinCshToInst")

	@MinCshToInst.deleter
	def MinCshToInst(self):
		del self._MinCshToInst
		self._MinCshToInst = None

	@property
	def MinPric(self):
		return self._MinPric

	@MinPric.setter
	def MinPric(self, value):
		self._MinPric = value if type(value) != auto else self.make_default("MinPric")

	@MinPric.deleter
	def MinPric(self):
		del self._MinPric
		self._MinPric = None

	@property
	def LastBidIncrmtPric(self):
		return self._LastBidIncrmtPric

	@LastBidIncrmtPric.setter
	def LastBidIncrmtPric(self, value):
		self._LastBidIncrmtPric = value if type(value) != auto else self.make_default("LastBidIncrmtPric")

	@LastBidIncrmtPric.deleter
	def LastBidIncrmtPric(self):
		del self._LastBidIncrmtPric
		self._LastBidIncrmtPric = None

	@property
	def OverSbcptDpstPric(self):
		return self._OverSbcptDpstPric

	@OverSbcptDpstPric.setter
	def OverSbcptDpstPric(self, value):
		self._OverSbcptDpstPric = value if type(value) != auto else self.make_default("OverSbcptDpstPric")

	@OverSbcptDpstPric.deleter
	def OverSbcptDpstPric(self):
		del self._OverSbcptDpstPric
		self._OverSbcptDpstPric = None

	@property
	def FrstBidIncrmtPric(self):
		return self._FrstBidIncrmtPric

	@FrstBidIncrmtPric.setter
	def FrstBidIncrmtPric(self, value):
		self._FrstBidIncrmtPric = value if type(value) != auto else self.make_default("FrstBidIncrmtPric")

	@FrstBidIncrmtPric.deleter
	def FrstBidIncrmtPric(self):
		del self._FrstBidIncrmtPric
		self._FrstBidIncrmtPric = None

	@property
	def MaxCshToInst(self):
		return self._MaxCshToInst

	@MaxCshToInst.setter
	def MaxCshToInst(self, value):
		self._MaxCshToInst = value if type(value) != auto else self.make_default("MaxCshToInst")

	@MaxCshToInst.deleter
	def MaxCshToInst(self):
		del self._MaxCshToInst
		self._MaxCshToInst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxPric', type=PriceFormat80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat81Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplCshToInst', type=PriceFormat61Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinCshToInst', type=PriceFormat61Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPric', type=PriceFormat80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastBidIncrmtPric', type=PriceFormat80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverSbcptDpstPric', type=PriceFormat81Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstBidIncrmtPric', type=PriceFormat80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCshToInst', type=PriceFormat61Choice, min=0, max=1, mutex_group=None, array=False),
	))

