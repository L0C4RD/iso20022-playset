from . import base_types
from .ContactAttributes5 import ContactAttributes5
from .AdditionalInformation15 import AdditionalInformation15
from .ISODate import ISODate

class OrderDesk1(base_types._BaseFieldType):

	__slots__ = ["_OrdrDsk", "_ClsrDts", "_AddtlInf"]
	@property
	def OrdrDsk(self):
		return self._OrdrDsk

	@OrdrDsk.setter
	def OrdrDsk(self, value):
		self._OrdrDsk = value if type(value) != auto else self.make_default("OrdrDsk")

	@OrdrDsk.deleter
	def OrdrDsk(self):
		del self._OrdrDsk
		self._OrdrDsk = None

	@property
	def ClsrDts(self):
		return self._ClsrDts

	@ClsrDts.setter
	def ClsrDts(self, value):
		self._ClsrDts = value if type(value) != auto else self.make_default("ClsrDts")

	@ClsrDts.deleter
	def ClsrDts(self):
		del self._ClsrDts
		self._ClsrDts = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrDsk', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrDts', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

