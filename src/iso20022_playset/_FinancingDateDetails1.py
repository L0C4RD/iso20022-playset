# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate

class FinancingDateDetails1(base_types._BaseFieldType):

	__slots__ = ["_BookDt", "_CdtDt", "_DbtDt"]
	@property
	def BookDt(self):
		return self._BookDt

	@BookDt.setter
	def BookDt(self, value):
		self._BookDt = value if value is not None else base_types.UninitialisedField(self, 'BookDt', ISODate, True)

	@BookDt.deleter
	def BookDt(self):
		del self._BookDt
		self._BookDt = base_types.UninitialisedField(self, 'BookDt', ISODate, True)

	@property
	def CdtDt(self):
		return self._CdtDt

	@CdtDt.setter
	def CdtDt(self, value):
		self._CdtDt = value if value is not None else base_types.UninitialisedField(self, 'CdtDt', ISODate, False)

	@CdtDt.deleter
	def CdtDt(self):
		del self._CdtDt
		self._CdtDt = base_types.UninitialisedField(self, 'CdtDt', ISODate, False)

	@property
	def DbtDt(self):
		return self._DbtDt

	@DbtDt.setter
	def DbtDt(self, value):
		self._DbtDt = value if value is not None else base_types.UninitialisedField(self, 'DbtDt', ISODate, False)

	@DbtDt.deleter
	def DbtDt(self):
		del self._DbtDt
		self._DbtDt = base_types.UninitialisedField(self, 'DbtDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookDt', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))