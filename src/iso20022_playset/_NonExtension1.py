from . import base_types
from ._CommunicationMethod1Choice import CommunicationMethod1Choice
from ._Max140Text import Max140Text
from ._Number import Number
from ._PartyType1Choice import PartyType1Choice
from ._PostalAddress6 import PostalAddress6

class NonExtension1(base_types._BaseFieldType):

	__slots__ = ["_NtfctnMtd", "_NtfctnPrd", "_NtfctnRcptAdr", "_NtfctnRcptNm", "_NtfctnRcptTp"]
	@property
	def NtfctnMtd(self):
		return self._NtfctnMtd

	@NtfctnMtd.setter
	def NtfctnMtd(self, value):
		self._NtfctnMtd = value if type(value) != base_types.auto else self.make_default("NtfctnMtd")

	@NtfctnMtd.deleter
	def NtfctnMtd(self):
		del self._NtfctnMtd
		self._NtfctnMtd = None

	@property
	def NtfctnPrd(self):
		return self._NtfctnPrd

	@NtfctnPrd.setter
	def NtfctnPrd(self, value):
		self._NtfctnPrd = value if type(value) != base_types.auto else self.make_default("NtfctnPrd")

	@NtfctnPrd.deleter
	def NtfctnPrd(self):
		del self._NtfctnPrd
		self._NtfctnPrd = None

	@property
	def NtfctnRcptAdr(self):
		return self._NtfctnRcptAdr

	@NtfctnRcptAdr.setter
	def NtfctnRcptAdr(self, value):
		self._NtfctnRcptAdr = value if type(value) != base_types.auto else self.make_default("NtfctnRcptAdr")

	@NtfctnRcptAdr.deleter
	def NtfctnRcptAdr(self):
		del self._NtfctnRcptAdr
		self._NtfctnRcptAdr = None

	@property
	def NtfctnRcptNm(self):
		return self._NtfctnRcptNm

	@NtfctnRcptNm.setter
	def NtfctnRcptNm(self, value):
		self._NtfctnRcptNm = value if type(value) != base_types.auto else self.make_default("NtfctnRcptNm")

	@NtfctnRcptNm.deleter
	def NtfctnRcptNm(self):
		del self._NtfctnRcptNm
		self._NtfctnRcptNm = None

	@property
	def NtfctnRcptTp(self):
		return self._NtfctnRcptTp

	@NtfctnRcptTp.setter
	def NtfctnRcptTp(self, value):
		self._NtfctnRcptTp = value if type(value) != base_types.auto else self.make_default("NtfctnRcptTp")

	@NtfctnRcptTp.deleter
	def NtfctnRcptTp(self):
		del self._NtfctnRcptTp
		self._NtfctnRcptTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnMtd', type=CommunicationMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnPrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcptAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcptNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcptTp', type=PartyType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

