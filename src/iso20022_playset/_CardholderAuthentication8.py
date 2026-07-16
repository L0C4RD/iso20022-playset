# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthenticationMethod7Code
from . import ContentInformationType10
from . import Max5000Binary
from . import OnLinePIN5
from . import TrueFalseIndicator

class CardholderAuthentication8(base_types._BaseFieldType):

	__slots__ = ["_AuthntcnMtd", "_AuthntcnVal", "_CrdhldrOnLinePIN", "_PrtctdAuthntcnVal", "_TknReqd"]
	@property
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnMtd', AuthenticationMethod7Code, False)

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = base_types.UninitialisedField(self, 'AuthntcnMtd', AuthenticationMethod7Code, False)

	@property
	def AuthntcnVal(self):
		return self._AuthntcnVal

	@AuthntcnVal.setter
	def AuthntcnVal(self, value):
		self._AuthntcnVal = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnVal', Max5000Binary, False)

	@AuthntcnVal.deleter
	def AuthntcnVal(self):
		del self._AuthntcnVal
		self._AuthntcnVal = base_types.UninitialisedField(self, 'AuthntcnVal', Max5000Binary, False)

	@property
	def CrdhldrOnLinePIN(self):
		return self._CrdhldrOnLinePIN

	@CrdhldrOnLinePIN.setter
	def CrdhldrOnLinePIN(self, value):
		self._CrdhldrOnLinePIN = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrOnLinePIN', OnLinePIN5, False)

	@CrdhldrOnLinePIN.deleter
	def CrdhldrOnLinePIN(self):
		del self._CrdhldrOnLinePIN
		self._CrdhldrOnLinePIN = base_types.UninitialisedField(self, 'CrdhldrOnLinePIN', OnLinePIN5, False)

	@property
	def PrtctdAuthntcnVal(self):
		return self._PrtctdAuthntcnVal

	@PrtctdAuthntcnVal.setter
	def PrtctdAuthntcnVal(self, value):
		self._PrtctdAuthntcnVal = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAuthntcnVal', ContentInformationType10, False)

	@PrtctdAuthntcnVal.deleter
	def PrtctdAuthntcnVal(self):
		del self._PrtctdAuthntcnVal
		self._PrtctdAuthntcnVal = base_types.UninitialisedField(self, 'PrtctdAuthntcnVal', ContentInformationType10, False)

	@property
	def TknReqd(self):
		return self._TknReqd

	@TknReqd.setter
	def TknReqd(self, value):
		self._TknReqd = value if value is not None else base_types.UninitialisedField(self, 'TknReqd', TrueFalseIndicator, False)

	@TknReqd.deleter
	def TknReqd(self):
		del self._TknReqd
		self._TknReqd = base_types.UninitialisedField(self, 'TknReqd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcnMtd', type=AuthenticationMethod7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnVal', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrOnLinePIN', type=OnLinePIN5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAuthntcnVal', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))