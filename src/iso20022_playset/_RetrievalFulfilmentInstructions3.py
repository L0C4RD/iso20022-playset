# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Address2 import Address2
from ._ContactBusiness1 import ContactBusiness1
from ._Max20KText import Max20KText
from ._Max35Text import Max35Text
from ._OutputFormat4Code import OutputFormat4Code
from ._PartyType19Code import PartyType19Code
from ._UserInterface8Code import UserInterface8Code

class RetrievalFulfilmentInstructions3(base_types._BaseFieldType):

	__slots__ = ["_ActlDlvryMtd", "_Ctct", "_EstblishdMtd", "_Frmt", "_PstlAdr", "_Rcpt", "_ReqdMtd", "_Tp", "_Trgt", "_Val"]
	@property
	def ActlDlvryMtd(self):
		return self._ActlDlvryMtd

	@ActlDlvryMtd.setter
	def ActlDlvryMtd(self, value):
		self._ActlDlvryMtd = value if type(value) != base_types.auto else self.make_default("ActlDlvryMtd")

	@ActlDlvryMtd.deleter
	def ActlDlvryMtd(self):
		del self._ActlDlvryMtd
		self._ActlDlvryMtd = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != base_types.auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def EstblishdMtd(self):
		return self._EstblishdMtd

	@EstblishdMtd.setter
	def EstblishdMtd(self, value):
		self._EstblishdMtd = value if type(value) != base_types.auto else self.make_default("EstblishdMtd")

	@EstblishdMtd.deleter
	def EstblishdMtd(self):
		del self._EstblishdMtd
		self._EstblishdMtd = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def ReqdMtd(self):
		return self._ReqdMtd

	@ReqdMtd.setter
	def ReqdMtd(self, value):
		self._ReqdMtd = value if type(value) != base_types.auto else self.make_default("ReqdMtd")

	@ReqdMtd.deleter
	def ReqdMtd(self):
		del self._ReqdMtd
		self._ReqdMtd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != base_types.auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlDlvryMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdMtd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyType19Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdMtd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=UserInterface8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Val', type=Max20KText, min=1, max=1, mutex_group=None, array=False),
	))