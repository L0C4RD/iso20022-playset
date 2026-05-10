from . import base_types
from ._ATMDepositedMediaItem1 import ATMDepositedMediaItem1
from ._ATMMediaType3Code import ATMMediaType3Code
from ._ATMMediaType4Code import ATMMediaType4Code
from ._Number import Number

class ATMDepositedMedia4(base_types._BaseFieldType):

	__slots__ = ["_AcctSeqNb", "_MdiaCtgy", "_MdiaItm", "_MdiaTp"]
	@property
	def AcctSeqNb(self):
		return self._AcctSeqNb

	@AcctSeqNb.setter
	def AcctSeqNb(self, value):
		self._AcctSeqNb = value if type(value) != base_types.auto else self.make_default("AcctSeqNb")

	@AcctSeqNb.deleter
	def AcctSeqNb(self):
		del self._AcctSeqNb
		self._AcctSeqNb = None

	@property
	def MdiaCtgy(self):
		return self._MdiaCtgy

	@MdiaCtgy.setter
	def MdiaCtgy(self, value):
		self._MdiaCtgy = value if type(value) != base_types.auto else self.make_default("MdiaCtgy")

	@MdiaCtgy.deleter
	def MdiaCtgy(self):
		del self._MdiaCtgy
		self._MdiaCtgy = None

	@property
	def MdiaItm(self):
		return self._MdiaItm

	@MdiaItm.setter
	def MdiaItm(self, value):
		self._MdiaItm = value if type(value) != base_types.auto else self.make_default("MdiaItm")

	@MdiaItm.deleter
	def MdiaItm(self):
		del self._MdiaItm
		self._MdiaItm = None

	@property
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if type(value) != base_types.auto else self.make_default("MdiaTp")

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaCtgy', type=ATMMediaType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaItm', type=ATMDepositedMediaItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=1, max=1, mutex_group=None, array=False),
	))

