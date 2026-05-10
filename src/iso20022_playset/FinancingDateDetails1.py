import base_types
import ISODate

class FinancingDateDetails1(base_types._BaseFieldType):

	__slots__ = ["_DbtDt", "_CdtDt", "_BookDt"]
	@property
	def DbtDt(self):
		return self._DbtDt

	@DbtDt.setter
	def DbtDt(self, value):
		self._DbtDt = value if type(value) != auto else self.make_default("DbtDt")

	@DbtDt.deleter
	def DbtDt(self):
		del self._DbtDt
		self._DbtDt = None

	@property
	def CdtDt(self):
		return self._CdtDt

	@CdtDt.setter
	def CdtDt(self, value):
		self._CdtDt = value if type(value) != auto else self.make_default("CdtDt")

	@CdtDt.deleter
	def CdtDt(self):
		del self._CdtDt
		self._CdtDt = None

	@property
	def BookDt(self):
		return self._BookDt

	@BookDt.setter
	def BookDt(self, value):
		self._BookDt = value if type(value) != auto else self.make_default("BookDt")

	@BookDt.deleter
	def BookDt(self):
		del self._BookDt
		self._BookDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookDt', type=ISODate, min=0, max=None, mutex_group=None, array=True),
	))

