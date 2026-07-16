# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53

class ExposureMetrics5(base_types._BaseFieldType):

	__slots__ = ["_CollMktVal", "_CshCollAmt"]
	@property
	def CollMktVal(self):
		return self._CollMktVal

	@CollMktVal.setter
	def CollMktVal(self, value):
		self._CollMktVal = value if value is not None else base_types.UninitialisedField(self, 'CollMktVal', AmountAndDirection53, False)

	@CollMktVal.deleter
	def CollMktVal(self):
		del self._CollMktVal
		self._CollMktVal = base_types.UninitialisedField(self, 'CollMktVal', AmountAndDirection53, False)

	@property
	def CshCollAmt(self):
		return self._CshCollAmt

	@CshCollAmt.setter
	def CshCollAmt(self, value):
		self._CshCollAmt = value if value is not None else base_types.UninitialisedField(self, 'CshCollAmt', AmountAndDirection53, False)

	@CshCollAmt.deleter
	def CshCollAmt(self):
		del self._CshCollAmt
		self._CshCollAmt = base_types.UninitialisedField(self, 'CshCollAmt', AmountAndDirection53, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCollAmt', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
	))