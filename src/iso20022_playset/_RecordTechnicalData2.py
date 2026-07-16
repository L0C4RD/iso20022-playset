# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledStatusReason15Code
from . import ISODateTime

class RecordTechnicalData2(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_RctDtTm"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', CancelledStatusReason15Code, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', CancelledStatusReason15Code, False)

	@property
	def RctDtTm(self):
		return self._RctDtTm

	@RctDtTm.setter
	def RctDtTm(self, value):
		self._RctDtTm = value if value is not None else base_types.UninitialisedField(self, 'RctDtTm', ISODateTime, False)

	@RctDtTm.deleter
	def RctDtTm(self):
		del self._RctDtTm
		self._RctDtTm = base_types.UninitialisedField(self, 'RctDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=CancelledStatusReason15Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))