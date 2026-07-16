# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Response2Code
from . import ResultDetail3Code

class ResponseType6(base_types._BaseFieldType):

	__slots__ = ["_AddtlRspn", "_Rspn", "_RspnDtl"]
	@property
	def AddtlRspn(self):
		return self._AddtlRspn

	@AddtlRspn.setter
	def AddtlRspn(self, value):
		self._AddtlRspn = value if value is not None else base_types.UninitialisedField(self, 'AddtlRspn', Max140Text, False)

	@AddtlRspn.deleter
	def AddtlRspn(self):
		del self._AddtlRspn
		self._AddtlRspn = base_types.UninitialisedField(self, 'AddtlRspn', Max140Text, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', Response2Code, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', Response2Code, False)

	@property
	def RspnDtl(self):
		return self._RspnDtl

	@RspnDtl.setter
	def RspnDtl(self, value):
		self._RspnDtl = value if value is not None else base_types.UninitialisedField(self, 'RspnDtl', ResultDetail3Code, False)

	@RspnDtl.deleter
	def RspnDtl(self):
		del self._RspnDtl
		self._RspnDtl = base_types.UninitialisedField(self, 'RspnDtl', ResultDetail3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRspn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDtl', type=ResultDetail3Code, min=0, max=1, mutex_group=None, array=False),
	))