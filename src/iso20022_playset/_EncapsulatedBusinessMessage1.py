from . import base_types
from ._xs:ID import xs:ID
from ._BusinessApplicationHeader1 import BusinessApplicationHeader1
from ._YesNoIndicator import YesNoIndicator
from ._StrictPayload import StrictPayload

class EncapsulatedBusinessMessage1(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_Prtl", "_Prfx", "_Msg"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def Msg(self):
		return self._Msg

	@Msg.setter
	def Msg(self, value):
		self._Msg = value if type(value) != base_types.auto else self.make_default("Msg")

	@Msg.deleter
	def Msg(self):
		del self._Msg
		self._Msg = None

	@property
	def Prfx(self):
		return self._Prfx

	@Prfx.setter
	def Prfx(self, value):
		self._Prfx = value if type(value) != base_types.auto else self.make_default("Prfx")

	@Prfx.deleter
	def Prfx(self):
		del self._Prfx
		self._Prfx = None

	@property
	def Prtl(self):
		return self._Prtl

	@Prtl.setter
	def Prtl(self, value):
		self._Prtl = value if type(value) != base_types.auto else self.make_default("Prtl")

	@Prtl.deleter
	def Prtl(self):
		del self._Prtl
		self._Prtl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=BusinessApplicationHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Msg', type=StrictPayload, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfx', type=XS_ID, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

