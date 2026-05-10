from . import base_types
from .AmountAndDirection53 import AmountAndDirection53

class ExposureMetrics5(base_types._BaseFieldType):

	__slots__ = ["_CshCollAmt", "_CollMktVal"]
	@property
	def CshCollAmt(self):
		return self._CshCollAmt

	@CshCollAmt.setter
	def CshCollAmt(self, value):
		self._CshCollAmt = value if type(value) != auto else self.make_default("CshCollAmt")

	@CshCollAmt.deleter
	def CshCollAmt(self):
		del self._CshCollAmt
		self._CshCollAmt = None

	@property
	def CollMktVal(self):
		return self._CollMktVal

	@CollMktVal.setter
	def CollMktVal(self, value):
		self._CollMktVal = value if type(value) != auto else self.make_default("CollMktVal")

	@CollMktVal.deleter
	def CollMktVal(self):
		del self._CollMktVal
		self._CollMktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCollAmt', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
	))

