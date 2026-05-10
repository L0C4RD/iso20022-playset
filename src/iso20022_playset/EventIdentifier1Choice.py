import base_types
import UTIIdentifier
import PostTradeRiskReductionIdentifier1

class EventIdentifier1Choice(base_types._BaseFieldType):

	__slots__ = ["_EvtIdr", "_PstTradRskRdctnIdr"]
	@property
	def EvtIdr(self):
		return self._EvtIdr

	@EvtIdr.setter
	def EvtIdr(self, value):
		self._EvtIdr = value if type(value) != auto else self.make_default("EvtIdr")

	@EvtIdr.deleter
	def EvtIdr(self):
		del self._EvtIdr
		self._EvtIdr = None

	@property
	def PstTradRskRdctnIdr(self):
		return self._PstTradRskRdctnIdr

	@PstTradRskRdctnIdr.setter
	def PstTradRskRdctnIdr(self, value):
		self._PstTradRskRdctnIdr = value if type(value) != auto else self.make_default("PstTradRskRdctnIdr")

	@PstTradRskRdctnIdr.deleter
	def PstTradRskRdctnIdr(self):
		del self._PstTradRskRdctnIdr
		self._PstTradRskRdctnIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PstTradRskRdctnIdr', type=PostTradeRiskReductionIdentifier1, min=0, max=1, mutex_group=1, array=False),
	))

