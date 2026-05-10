from . import base_types
from .Max8Text import Max8Text
from .GenericIdentification90 import GenericIdentification90
from .TMSTrigger1 import TMSTrigger1
from .ResponseType10 import ResponseType10

class AuthorisationResult19(base_types._BaseFieldType):

	__slots__ = ["_AuthstnNtty", "_RspnToAuthstn", "_AuthstnCd", "_TMSTrggr"]
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
	def RspnToAuthstn(self):
		return self._RspnToAuthstn

	@RspnToAuthstn.setter
	def RspnToAuthstn(self, value):
		self._RspnToAuthstn = value if type(value) != base_types.auto else self.make_default("RspnToAuthstn")

	@RspnToAuthstn.deleter
	def RspnToAuthstn(self):
		del self._RspnToAuthstn
		self._RspnToAuthstn = None

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
	def TMSTrggr(self):
		return self._TMSTrggr

	@TMSTrggr.setter
	def TMSTrggr(self, value):
		self._TMSTrggr = value if type(value) != base_types.auto else self.make_default("TMSTrggr")

	@TMSTrggr.deleter
	def TMSTrggr(self):
		del self._TMSTrggr
		self._TMSTrggr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthstnNtty', type=GenericIdentification90, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnToAuthstn', type=ResponseType10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnCd', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSTrggr', type=TMSTrigger1, min=0, max=1, mutex_group=None, array=False),
	))

