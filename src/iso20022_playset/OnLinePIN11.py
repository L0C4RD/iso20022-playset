import base_types
import Max35Text
import ContentInformationType40
import PINFormat3Code

class OnLinePIN11(base_types._BaseFieldType):

	__slots__ = ["_NcrptdPINBlck", "_PINFrmt", "_AddtlInpt"]
	@property
	def NcrptdPINBlck(self):
		return self._NcrptdPINBlck

	@NcrptdPINBlck.setter
	def NcrptdPINBlck(self, value):
		self._NcrptdPINBlck = value if type(value) != auto else self.make_default("NcrptdPINBlck")

	@NcrptdPINBlck.deleter
	def NcrptdPINBlck(self):
		del self._NcrptdPINBlck
		self._NcrptdPINBlck = None

	@property
	def PINFrmt(self):
		return self._PINFrmt

	@PINFrmt.setter
	def PINFrmt(self, value):
		self._PINFrmt = value if type(value) != auto else self.make_default("PINFrmt")

	@PINFrmt.deleter
	def PINFrmt(self):
		del self._PINFrmt
		self._PINFrmt = None

	@property
	def AddtlInpt(self):
		return self._AddtlInpt

	@AddtlInpt.setter
	def AddtlInpt(self, value):
		self._AddtlInpt = value if type(value) != auto else self.make_default("AddtlInpt")

	@AddtlInpt.deleter
	def AddtlInpt(self):
		del self._AddtlInpt
		self._AddtlInpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NcrptdPINBlck', type=ContentInformationType40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINFrmt', type=PINFormat3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInpt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

