# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import ResponseType1Choice

class Response1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_RspnTpDtls"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def RspnTpDtls(self):
		return self._RspnTpDtls

	@RspnTpDtls.setter
	def RspnTpDtls(self, value):
		self._RspnTpDtls = value if value is not None else base_types.UninitialisedField(self, 'RspnTpDtls', ResponseType1Choice, True)

	@RspnTpDtls.deleter
	def RspnTpDtls(self):
		del self._RspnTpDtls
		self._RspnTpDtls = base_types.UninitialisedField(self, 'RspnTpDtls', ResponseType1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnTpDtls', type=ResponseType1Choice, min=1, max=None, mutex_group=None, array=True),
	))