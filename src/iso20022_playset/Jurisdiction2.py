from . import base_types
import Max35Text
import TrueFalseIndicator

class Jurisdiction2(base_types._BaseFieldType):

	__slots__ = ["_DmstQlfctn", "_DmstInd"]
	@property
	def DmstQlfctn(self):
		return self._DmstQlfctn

	@DmstQlfctn.setter
	def DmstQlfctn(self, value):
		self._DmstQlfctn = value if type(value) != auto else self.make_default("DmstQlfctn")

	@DmstQlfctn.deleter
	def DmstQlfctn(self):
		del self._DmstQlfctn
		self._DmstQlfctn = None

	@property
	def DmstInd(self):
		return self._DmstInd

	@DmstInd.setter
	def DmstInd(self, value):
		self._DmstInd = value if type(value) != auto else self.make_default("DmstInd")

	@DmstInd.deleter
	def DmstInd(self):
		del self._DmstInd
		self._DmstInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmstQlfctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmstInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

