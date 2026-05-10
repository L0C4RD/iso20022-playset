import base_types
import NDFOpeningFixing1Choice
import YesNoIndicator

class NonDeliverableForwardConditions1(base_types._BaseFieldType):

	__slots__ = ["_OpngInd", "_OpngFxgConds"]
	@property
	def OpngInd(self):
		return self._OpngInd

	@OpngInd.setter
	def OpngInd(self, value):
		self._OpngInd = value if type(value) != auto else self.make_default("OpngInd")

	@OpngInd.deleter
	def OpngInd(self):
		del self._OpngInd
		self._OpngInd = None

	@property
	def OpngFxgConds(self):
		return self._OpngFxgConds

	@OpngFxgConds.setter
	def OpngFxgConds(self, value):
		self._OpngFxgConds = value if type(value) != auto else self.make_default("OpngFxgConds")

	@OpngFxgConds.deleter
	def OpngFxgConds(self):
		del self._OpngFxgConds
		self._OpngFxgConds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngFxgConds', type=NDFOpeningFixing1Choice, min=1, max=1, mutex_group=None, array=False),
	))

