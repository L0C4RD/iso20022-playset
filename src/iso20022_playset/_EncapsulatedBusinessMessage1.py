# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessApplicationHeader1
from . import StrictPayload
from . import YesNoIndicator
from . import xs:ID

class EncapsulatedBusinessMessage1(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_Msg", "_Prfx", "_Prtl"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', BusinessApplicationHeader1, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', BusinessApplicationHeader1, False)

	@property
	def Msg(self):
		return self._Msg

	@Msg.setter
	def Msg(self, value):
		self._Msg = value if value is not None else base_types.UninitialisedField(self, 'Msg', StrictPayload, False)

	@Msg.deleter
	def Msg(self):
		del self._Msg
		self._Msg = base_types.UninitialisedField(self, 'Msg', StrictPayload, False)

	@property
	def Prfx(self):
		return self._Prfx

	@Prfx.setter
	def Prfx(self, value):
		self._Prfx = value if value is not None else base_types.UninitialisedField(self, 'Prfx', xs:ID, False)

	@Prfx.deleter
	def Prfx(self):
		del self._Prfx
		self._Prfx = base_types.UninitialisedField(self, 'Prfx', xs:ID, False)

	@property
	def Prtl(self):
		return self._Prtl

	@Prtl.setter
	def Prtl(self, value):
		self._Prtl = value if value is not None else base_types.UninitialisedField(self, 'Prtl', YesNoIndicator, False)

	@Prtl.deleter
	def Prtl(self):
		del self._Prtl
		self._Prtl = base_types.UninitialisedField(self, 'Prtl', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=BusinessApplicationHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Msg', type=StrictPayload, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfx', type=XS_ID, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))