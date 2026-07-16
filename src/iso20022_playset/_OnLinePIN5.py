# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType10
from . import Max35Text
from . import PINFormat4Code

class OnLinePIN5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInpt", "_NcrptdPINBlck", "_PINFrmt"]
	@property
	def AddtlInpt(self):
		return self._AddtlInpt

	@AddtlInpt.setter
	def AddtlInpt(self, value):
		self._AddtlInpt = value if value is not None else base_types.UninitialisedField(self, 'AddtlInpt', Max35Text, False)

	@AddtlInpt.deleter
	def AddtlInpt(self):
		del self._AddtlInpt
		self._AddtlInpt = base_types.UninitialisedField(self, 'AddtlInpt', Max35Text, False)

	@property
	def NcrptdPINBlck(self):
		return self._NcrptdPINBlck

	@NcrptdPINBlck.setter
	def NcrptdPINBlck(self, value):
		self._NcrptdPINBlck = value if value is not None else base_types.UninitialisedField(self, 'NcrptdPINBlck', ContentInformationType10, False)

	@NcrptdPINBlck.deleter
	def NcrptdPINBlck(self):
		del self._NcrptdPINBlck
		self._NcrptdPINBlck = base_types.UninitialisedField(self, 'NcrptdPINBlck', ContentInformationType10, False)

	@property
	def PINFrmt(self):
		return self._PINFrmt

	@PINFrmt.setter
	def PINFrmt(self, value):
		self._PINFrmt = value if value is not None else base_types.UninitialisedField(self, 'PINFrmt', PINFormat4Code, False)

	@PINFrmt.deleter
	def PINFrmt(self):
		del self._PINFrmt
		self._PINFrmt = base_types.UninitialisedField(self, 'PINFrmt', PINFormat4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInpt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdPINBlck', type=ContentInformationType10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINFrmt', type=PINFormat4Code, min=1, max=1, mutex_group=None, array=False),
	))