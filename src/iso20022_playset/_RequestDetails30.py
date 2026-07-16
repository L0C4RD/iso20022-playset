# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification242Choice

class RequestDetails30(base_types._BaseFieldType):

	__slots__ = ["_AddtlReqInf", "_RqstrId", "_Tp"]
	@property
	def AddtlReqInf(self):
		return self._AddtlReqInf

	@AddtlReqInf.setter
	def AddtlReqInf(self, value):
		self._AddtlReqInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlReqInf', Max35Text, True)

	@AddtlReqInf.deleter
	def AddtlReqInf(self):
		del self._AddtlReqInf
		self._AddtlReqInf = base_types.UninitialisedField(self, 'AddtlReqInf', Max35Text, True)

	@property
	def RqstrId(self):
		return self._RqstrId

	@RqstrId.setter
	def RqstrId(self, value):
		self._RqstrId = value if value is not None else base_types.UninitialisedField(self, 'RqstrId', PartyIdentification242Choice, False)

	@RqstrId.deleter
	def RqstrId(self):
		del self._RqstrId
		self._RqstrId = base_types.UninitialisedField(self, 'RqstrId', PartyIdentification242Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlReqInf', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RqstrId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))