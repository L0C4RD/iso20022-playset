# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Max35Text

class ResponseDetails1(base_types._BaseFieldType):

	__slots__ = ["_AddtlDtls", "_RspnCd"]
	@property
	def AddtlDtls(self):
		return self._AddtlDtls

	@AddtlDtls.setter
	def AddtlDtls(self, value):
		self._AddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlDtls', Max350Text, False)

	@AddtlDtls.deleter
	def AddtlDtls(self):
		del self._AddtlDtls
		self._AddtlDtls = base_types.UninitialisedField(self, 'AddtlDtls', Max350Text, False)

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if value is not None else base_types.UninitialisedField(self, 'RspnCd', Max35Text, False)

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = base_types.UninitialisedField(self, 'RspnCd', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))