# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMFeeComponent1 import ATMFeeComponent1
from ._Action7 import Action7
from ._Max8Text import Max8Text
from ._PartyType16Code import PartyType16Code
from ._ResponseType12 import ResponseType12
from ._ResponseType8 import ResponseType8

class AuthorisationResult20(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_AuthstnCd", "_AuthstnNtty", "_AuthstnRspn", "_FeeToAdd", "_RspnTrac"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != base_types.auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def AuthstnCd(self):
		return self._AuthstnCd

	@AuthstnCd.setter
	def AuthstnCd(self, value):
		self._AuthstnCd = value if type(value) != base_types.auto else self.make_default("AuthstnCd")

	@AuthstnCd.deleter
	def AuthstnCd(self):
		del self._AuthstnCd
		self._AuthstnCd = None

	@property
	def AuthstnNtty(self):
		return self._AuthstnNtty

	@AuthstnNtty.setter
	def AuthstnNtty(self, value):
		self._AuthstnNtty = value if type(value) != base_types.auto else self.make_default("AuthstnNtty")

	@AuthstnNtty.deleter
	def AuthstnNtty(self):
		del self._AuthstnNtty
		self._AuthstnNtty = None

	@property
	def AuthstnRspn(self):
		return self._AuthstnRspn

	@AuthstnRspn.setter
	def AuthstnRspn(self, value):
		self._AuthstnRspn = value if type(value) != base_types.auto else self.make_default("AuthstnRspn")

	@AuthstnRspn.deleter
	def AuthstnRspn(self):
		del self._AuthstnRspn
		self._AuthstnRspn = None

	@property
	def FeeToAdd(self):
		return self._FeeToAdd

	@FeeToAdd.setter
	def FeeToAdd(self, value):
		self._FeeToAdd = value if type(value) != base_types.auto else self.make_default("FeeToAdd")

	@FeeToAdd.deleter
	def FeeToAdd(self):
		del self._FeeToAdd
		self._FeeToAdd = None

	@property
	def RspnTrac(self):
		return self._RspnTrac

	@RspnTrac.setter
	def RspnTrac(self, value):
		self._RspnTrac = value if type(value) != base_types.auto else self.make_default("RspnTrac")

	@RspnTrac.deleter
	def RspnTrac(self):
		del self._RspnTrac
		self._RspnTrac = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=Action7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnCd', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnNtty', type=PartyType16Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FeeToAdd', type=ATMFeeComponent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnTrac', type=ResponseType8, min=0, max=None, mutex_group=None, array=True),
	))