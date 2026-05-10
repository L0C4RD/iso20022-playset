from . import base_types
from .Max52Text import Max52Text
from .ISODateTime import ISODateTime

class DisseminationData1(base_types._BaseFieldType):

	__slots__ = ["_DssmntnIdr", "_OrgnlDssmntnIdr", "_TmStmp"]
	@property
	def DssmntnIdr(self):
		return self._DssmntnIdr

	@DssmntnIdr.setter
	def DssmntnIdr(self, value):
		self._DssmntnIdr = value if type(value) != base_types.auto else self.make_default("DssmntnIdr")

	@DssmntnIdr.deleter
	def DssmntnIdr(self):
		del self._DssmntnIdr
		self._DssmntnIdr = None

	@property
	def OrgnlDssmntnIdr(self):
		return self._OrgnlDssmntnIdr

	@OrgnlDssmntnIdr.setter
	def OrgnlDssmntnIdr(self, value):
		self._OrgnlDssmntnIdr = value if type(value) != base_types.auto else self.make_default("OrgnlDssmntnIdr")

	@OrgnlDssmntnIdr.deleter
	def OrgnlDssmntnIdr(self):
		del self._OrgnlDssmntnIdr
		self._OrgnlDssmntnIdr = None

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != base_types.auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DssmntnIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDssmntnIdr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

