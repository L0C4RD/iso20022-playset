import base_types
import ContentInformationType38
import Header41
import MessageStatusResponse9

class SaleToPOIMessageStatusResponseV07(base_types._BaseFieldType):

	__slots__ = ["_StsRspn", "_Hdr", "_SctyTrlr"]
	@property
	def StsRspn(self):
		return self._StsRspn

	@StsRspn.setter
	def StsRspn(self, value):
		self._StsRspn = value if type(value) != auto else self.make_default("StsRspn")

	@StsRspn.deleter
	def StsRspn(self):
		del self._StsRspn
		self._StsRspn = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsRspn', type=MessageStatusResponse9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))

