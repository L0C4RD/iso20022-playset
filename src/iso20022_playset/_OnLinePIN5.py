# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType10 import ContentInformationType10
from ._Max35Text import Max35Text
from ._PINFormat4Code import PINFormat4Code

class OnLinePIN5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInpt", "_NcrptdPINBlck", "_PINFrmt"]
	@property
	def AddtlInpt(self):
		return self._AddtlInpt

	@AddtlInpt.setter
	def AddtlInpt(self, value):
		self._AddtlInpt = value if type(value) != base_types.auto else self.make_default("AddtlInpt")

	@AddtlInpt.deleter
	def AddtlInpt(self):
		del self._AddtlInpt
		self._AddtlInpt = None

	@property
	def NcrptdPINBlck(self):
		return self._NcrptdPINBlck

	@NcrptdPINBlck.setter
	def NcrptdPINBlck(self, value):
		self._NcrptdPINBlck = value if type(value) != base_types.auto else self.make_default("NcrptdPINBlck")

	@NcrptdPINBlck.deleter
	def NcrptdPINBlck(self):
		del self._NcrptdPINBlck
		self._NcrptdPINBlck = None

	@property
	def PINFrmt(self):
		return self._PINFrmt

	@PINFrmt.setter
	def PINFrmt(self, value):
		self._PINFrmt = value if type(value) != base_types.auto else self.make_default("PINFrmt")

	@PINFrmt.deleter
	def PINFrmt(self):
		del self._PINFrmt
		self._PINFrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInpt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdPINBlck', type=ContentInformationType10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINFrmt', type=PINFormat4Code, min=1, max=1, mutex_group=None, array=False),
	))