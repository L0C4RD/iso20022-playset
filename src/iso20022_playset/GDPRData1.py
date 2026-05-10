from . import base_types
import ISODate
import YesNoIndicator
import GDPRDataConsent1Choice

class GDPRData1(base_types._BaseFieldType):

	__slots__ = ["_CnsntInd", "_CnsntDt", "_CnsntTp"]
	@property
	def CnsntInd(self):
		return self._CnsntInd

	@CnsntInd.setter
	def CnsntInd(self, value):
		self._CnsntInd = value if type(value) != auto else self.make_default("CnsntInd")

	@CnsntInd.deleter
	def CnsntInd(self):
		del self._CnsntInd
		self._CnsntInd = None

	@property
	def CnsntDt(self):
		return self._CnsntDt

	@CnsntDt.setter
	def CnsntDt(self, value):
		self._CnsntDt = value if type(value) != auto else self.make_default("CnsntDt")

	@CnsntDt.deleter
	def CnsntDt(self):
		del self._CnsntDt
		self._CnsntDt = None

	@property
	def CnsntTp(self):
		return self._CnsntTp

	@CnsntTp.setter
	def CnsntTp(self, value):
		self._CnsntTp = value if type(value) != auto else self.make_default("CnsntTp")

	@CnsntTp.deleter
	def CnsntTp(self):
		del self._CnsntTp
		self._CnsntTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnsntInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=GDPRDataConsent1Choice, min=1, max=1, mutex_group=None, array=False),
	))

