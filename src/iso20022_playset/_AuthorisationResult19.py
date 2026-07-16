# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification90
from . import Max8Text
from . import ResponseType10
from . import TMSTrigger1

class AuthorisationResult19(base_types._BaseFieldType):

	__slots__ = ["_AuthstnCd", "_AuthstnNtty", "_RspnToAuthstn", "_TMSTrggr"]
	@property
	def AuthstnCd(self):
		return self._AuthstnCd

	@AuthstnCd.setter
	def AuthstnCd(self, value):
		self._AuthstnCd = value if value is not None else base_types.UninitialisedField(self, 'AuthstnCd', Max8Text, False)

	@AuthstnCd.deleter
	def AuthstnCd(self):
		del self._AuthstnCd
		self._AuthstnCd = base_types.UninitialisedField(self, 'AuthstnCd', Max8Text, False)

	@property
	def AuthstnNtty(self):
		return self._AuthstnNtty

	@AuthstnNtty.setter
	def AuthstnNtty(self, value):
		self._AuthstnNtty = value if value is not None else base_types.UninitialisedField(self, 'AuthstnNtty', GenericIdentification90, False)

	@AuthstnNtty.deleter
	def AuthstnNtty(self):
		del self._AuthstnNtty
		self._AuthstnNtty = base_types.UninitialisedField(self, 'AuthstnNtty', GenericIdentification90, False)

	@property
	def RspnToAuthstn(self):
		return self._RspnToAuthstn

	@RspnToAuthstn.setter
	def RspnToAuthstn(self, value):
		self._RspnToAuthstn = value if value is not None else base_types.UninitialisedField(self, 'RspnToAuthstn', ResponseType10, False)

	@RspnToAuthstn.deleter
	def RspnToAuthstn(self):
		del self._RspnToAuthstn
		self._RspnToAuthstn = base_types.UninitialisedField(self, 'RspnToAuthstn', ResponseType10, False)

	@property
	def TMSTrggr(self):
		return self._TMSTrggr

	@TMSTrggr.setter
	def TMSTrggr(self, value):
		self._TMSTrggr = value if value is not None else base_types.UninitialisedField(self, 'TMSTrggr', TMSTrigger1, False)

	@TMSTrggr.deleter
	def TMSTrggr(self):
		del self._TMSTrggr
		self._TMSTrggr = base_types.UninitialisedField(self, 'TMSTrggr', TMSTrigger1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthstnCd', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnNtty', type=GenericIdentification90, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnToAuthstn', type=ResponseType10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSTrggr', type=TMSTrigger1, min=0, max=1, mutex_group=None, array=False),
	))