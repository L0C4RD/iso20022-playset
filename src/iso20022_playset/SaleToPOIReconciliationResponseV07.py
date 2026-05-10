import base_types
import ContentInformationType38
import ReconciliationResponse10
import Header41

class SaleToPOIReconciliationResponseV07(base_types._BaseFieldType):

	__slots__ = ["_RcncltnRspn", "_Hdr", "_SctyTrlr"]
	@property
	def RcncltnRspn(self):
		return self._RcncltnRspn

	@RcncltnRspn.setter
	def RcncltnRspn(self, value):
		self._RcncltnRspn = value if type(value) != auto else self.make_default("RcncltnRspn")

	@RcncltnRspn.deleter
	def RcncltnRspn(self):
		del self._RcncltnRspn
		self._RcncltnRspn = None

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
		base_types.FieldEntry(name='RcncltnRspn', type=ReconciliationResponse10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))

